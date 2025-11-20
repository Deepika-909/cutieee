import { fileURLToPath } from "url";
import { dirname } from "path";
import { Builder, By, until } from "selenium-webdriver";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function runTest() {
  const driver = await new Builder().forBrowser("chrome").build();
  try {
    await driver.get("file://" + __dirname + "/index.html");
    await driver.findElement(By.id("num1")).sendKeys("10");
    await driver.findElement(By.id("num2")).sendKeys("50");
    await driver.findElement(By.id("add")).click();

    const resultText = await driver
      .findElement(By.id("result"))
      .getText();

    console.log(`10 + 50 = ${resultText}`);

    await driver.sleep(15000);

  } finally {
    await driver.quit();
  }
}

runTest();