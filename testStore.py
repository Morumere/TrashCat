
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  store_button_path = "/UICamera/Loadout/StoreButton"
  character_path = "/Canvas/Background/TabsSwitch/Character"
  accesories_path = "/Canvas/Background/TabsSwitch/Accesories"
  themes_path = "/Canvas/Background/TabsSwitch/Themes"
  button_path = "/Canvas/Background/Button"

  @classmethod
  def setUp(self):
    self.alt_driver = AltDriver(host="127.0.0.1", port=13000, app_name="__default__")

  # You might want to load the scene here
  #   self.alt_driver.load_scene("Start", True)

  @classmethod
  def tearDown(self):
    self.alt_driver.stop()

  def test(self):
    self.alt_driver.load_scene("Start", True)
    start_button = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button.click()
    store_button = self.alt_driver.wait_for_object(By.PATH, self.store_button_path, timeout=20)
    store_button.click()
    character = self.alt_driver.wait_for_object(By.PATH, self.character_path, timeout=20)
    character.click()
    accesories = self.alt_driver.wait_for_object(By.PATH, self.accesories_path, timeout=20)
    accesories.click()
    themes = self.alt_driver.wait_for_object(By.PATH, self.themes_path, timeout=20)
    themes.click()
    button = self.alt_driver.wait_for_object(By.PATH, self.button_path, timeout=20)
    button.click()
    self.alt_driver.load_scene("Start", True)
