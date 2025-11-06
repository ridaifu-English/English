#!/usr/bin/env node
/**
 * Export HTML slides to PowerPoint (PPTX) format
 * Uses PptxGenJS + Puppeteer for high-quality exports
 * 
 * Usage: node export-to-pptx.js <slide_directory> [output_name.pptx]
 * 
 * Example: node export-to-pptx.js ../expressions-using-"that" expressions.pptx
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');
const PptxGenJS = require('pptxgenjs');

async function captureSlides(slideDir) {
  const slidePath = path.resolve(slideDir);
  
  if (!fs.existsSync(slidePath)) {
    console.error(`Error: Directory '${slidePath}' not found`);
    process.exit(1);
  }
  
  // Find all slide HTML files
  const files = fs.readdirSync(slidePath)
    .filter(f => f.match(/^slide\d+\.html$/))
    .sort((a, b) => {
      const numA = parseInt(a.match(/\d+/)[0]);
      const numB = parseInt(b.match(/\d+/)[0]);
      return numA - numB;
    });
  
  if (files.length === 0) {
    console.error(`Error: No slide*.html files found in '${slidePath}'`);
    process.exit(1);
  }
  
  console.log(`Found ${files.length} slides`);
  console.log('Launching browser...');
  
  let browser;
  try {
    browser = await puppeteer.launch({
      headless: 'new',
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--disable-gpu'
      ],
      timeout: 60000
    });
    
    console.log('Browser launched successfully');
    
    const page = await browser.newPage();
    
    // Set longer timeout for navigation
    page.setDefaultNavigationTimeout(30000);
    page.setDefaultTimeout(30000);
    
    await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 2 });
    
    const screenshots = [];
    
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const filePath = path.join(slidePath, file);
      const fileUrl = `file://${filePath}`;
      
      console.log(`Capturing slide ${i + 1}/${files.length}: ${file}`);
      
      try {
        // Use domcontentloaded instead of networkidle0 for local files
        await page.goto(fileUrl, { 
          waitUntil: 'domcontentloaded',
          timeout: 30000
        });
        
        // Wait for fonts and icons to load
        await page.waitForTimeout(1000);
        
        // Wait for any Lucide icons to be created
        await page.evaluate(() => {
          return new Promise(resolve => {
            setTimeout(resolve, 500);
          });
        });
        
        // Take screenshot
        const screenshot = await page.screenshot({
          type: 'png',
          encoding: 'base64',
          fullPage: false
        });
        
        screenshots.push({
          name: file,
          data: screenshot
        });
        
      } catch (error) {
        console.error(`  ✗ Error capturing ${file}: ${error.message}`);
        console.log('  Continuing with next slide...');
      }
    }
    
    await browser.close();
    console.log('Browser closed');
    
    if (screenshots.length === 0) {
      throw new Error('No slides were captured successfully');
    }
    
    return screenshots;
    
  } catch (error) {
    if (browser) {
      await browser.close();
    }
    throw error;
  }
}

async function createPowerPoint(screenshots, outputPath) {
  console.log('Creating PowerPoint...');
  
  const pptx = new PptxGenJS();
  
  // Set presentation dimensions (16:9 ratio)
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Slide Generator';
  pptx.company = 'English Teaching Materials';
  pptx.revision = '1';
  pptx.subject = 'Educational Slides';
  pptx.title = path.basename(outputPath, '.pptx');
  
  for (let i = 0; i < screenshots.length; i++) {
    const screenshot = screenshots[i];
    console.log(`Adding slide ${i + 1}/${screenshots.length}: ${screenshot.name}`);
    
    const slide = pptx.addSlide();
    
    // Add screenshot as image covering entire slide
    slide.addImage({
      data: `data:image/png;base64,${screenshot.data}`,
      x: 0,
      y: 0,
      w: '100%',
      h: '100%'
    });
  }
  
  // Save the presentation
  await pptx.writeFile({ fileName: outputPath });
  console.log(`\n✓ Successfully created: ${outputPath}`);
}

async function main() {
  const args = process.argv.slice(2);
  
  if (args.length < 1) {
    console.log('Usage: node export-to-pptx.js <slide_directory> [output_name.pptx]');
    console.log('\nExample:');
    console.log('  node export-to-pptx.js ../expressions-using-"that" expressions.pptx');
    console.log('  node export-to-pptx.js ../inanimate-subject');
    process.exit(1);
  }
  
  const slideDir = args[0];
  let outputName = args[1];
  
  if (!outputName) {
    const dirName = path.basename(path.resolve(slideDir));
    outputName = `${dirName}.pptx`;
  }
  
  const outputPath = path.resolve(slideDir, outputName);
  
  try {
    // Capture all slides
    const screenshots = await captureSlides(slideDir);
    
    // Create PowerPoint
    await createPowerPoint(screenshots, outputPath);
    
    console.log('\n✓ Export complete!');
  } catch (error) {
    console.error('\n✗ Error:', error.message);
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { captureSlides, createPowerPoint };

