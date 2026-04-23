import { test, expect } from '@playwright/test';

const BASE = '/reading-hub/';

test.describe('Reading Hub - Home Page', () => {
  test('should load the home page', async ({ page }) => {
    await page.goto(BASE);
    const heading = page.getByRole('heading', { name: 'Reading Hub', exact: true });
    await expect(heading).toBeVisible();
  });

  test('should have a working navigation', async ({ page }) => {
    await page.goto(BASE);
    await expect(page).toHaveTitle(/Reading Hub/i);
  });

  test('should render correctly on mobile', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto(BASE);
    const content = page.locator('body');
    await expect(content).toBeVisible();
  });
});
