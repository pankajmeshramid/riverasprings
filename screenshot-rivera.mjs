import { chromium } from 'playwright';
const browser = await chromium.launch();

async function captureFullPage(page, path) {
  // Scroll through the entire page to trigger IntersectionObserver reveals
  const totalHeight = await page.evaluate(() => document.body.scrollHeight);
  const viewportHeight = await page.evaluate(() => window.innerHeight);
  for (let y = 0; y < totalHeight; y += viewportHeight * 0.5) {
    await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
    await page.waitForTimeout(300);
  }
  // Scroll back to top and wait for animations to settle
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(500);
  await page.screenshot({ path, fullPage: true });
}

// Desktop
const dp = await browser.newPage();
await dp.setViewportSize({ width: 1440, height: 900 });
await dp.goto('file:///C:/Users/PANKAJ/rivera-springs.html', { waitUntil: 'networkidle', timeout: 30000 });
await dp.waitForTimeout(2000);
await captureFullPage(dp, 'C:/Users/PANKAJ/rivera-desktop.png');

// Mobile
const mp = await browser.newPage();
await mp.setViewportSize({ width: 390, height: 844 });
await mp.goto('file:///C:/Users/PANKAJ/rivera-springs.html', { waitUntil: 'networkidle', timeout: 30000 });
await mp.waitForTimeout(2000);
await captureFullPage(mp, 'C:/Users/PANKAJ/rivera-mobile.png');

await browser.close();
console.log('Done');
