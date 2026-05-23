const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const PUBLIC_DIR = path.join(__dirname, 'public', 'images');
const SRC_DIR = path.join(__dirname, 'src');
const SCRATCH_DIR = path.join(__dirname, '.gemini', 'antigravity', 'brain', '174a48da-1ad0-497d-984a-8ed43ba6e259', 'scratch');

async function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat && stat.isDirectory()) {
      results = results.concat(await walk(filePath));
    } else {
      results.push(filePath);
    }
  }
  return results;
}

async function optimizeImages() {
  console.log('Finding images...');
  const files = await walk(PUBLIC_DIR);
  const extensionsToConvert = ['.png', '.jpg', '.jpeg'];
  
  const replacements = [];

  for (const filePath of files) {
    const ext = path.extname(filePath).toLowerCase();
    
    // We also want to re-compress existing webp files if they are too large
    if (extensionsToConvert.includes(ext) || ext === '.webp') {
      const parsed = path.parse(filePath);
      const newPath = path.join(parsed.dir, parsed.name + '.webp');
      
      try {
        const image = sharp(filePath);
        const metadata = await image.metadata();
        
        let sharpInst = image;
        // Resize if it's too big (width > 800)
        if (metadata.width > 800) {
          sharpInst = sharpInst.resize({ width: 800, withoutEnlargement: true });
        }
        
        // Output to webp with high compression
        await sharpInst.webp({ quality: 75, effort: 6 }).toFile(newPath + '.tmp');
        
        // Remove original and rename new
        if (filePath !== newPath) {
          fs.unlinkSync(filePath);
        }
        fs.renameSync(newPath + '.tmp', newPath);
        
        // Record replacement for source code updates
        if (filePath !== newPath) {
          // Get the relative path for HTML src
          const oldSrc = filePath.split('/public')[1];
          const newSrc = newPath.split('/public')[1];
          replacements.push({ oldSrc, newSrc });
        }
        
        console.log(`Optimized: ${filePath} -> ${newPath}`);
      } catch (err) {
        console.error(`Failed to process ${filePath}:`, err);
      }
    }
  }

  if (replacements.length > 0) {
    console.log(`Updating source files with ${replacements.length} replacements...`);
    const srcFiles = await walk(SRC_DIR);
    let allFiles = srcFiles.filter(f => f.endsWith('.astro') || f.endsWith('.js') || f.endsWith('.css'));
    
    // Also check rebuild script if it exists
    const rebuildScript = path.join(__dirname, 'scratch', 'rebuild_all_pages.py');
    if (fs.existsSync(rebuildScript)) allFiles.push(rebuildScript);

    for (const file of allFiles) {
      let content = fs.readFileSync(file, 'utf8');
      let changed = false;
      
      for (const {oldSrc, newSrc} of replacements) {
        // Simple string replace for all occurrences
        if (content.includes(oldSrc)) {
          content = content.split(oldSrc).join(newSrc);
          changed = true;
        }
      }
      
      if (changed) {
        fs.writeFileSync(file, content);
        console.log(`Updated references in: ${file}`);
      }
    }
  }
  
  console.log('Done!');
}

optimizeImages();
