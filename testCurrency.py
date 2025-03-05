
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  store_button_path = "/UICamera/Loadout/StoreButton"
  store_title_path = "/Canvas/Background/StoreTitle"
  coins_counter_path = "/Canvas/Background/Coin/CoinsCounter"

  @classmethod
  def setUp(self):
    self.alt_driver = AltDriver(host="127.0.0.1", port=13000, app_name="__default__")

  # You might want to load the scene here
  #   self.alt_driver.load_scene("Main", True)

  @classmethod
  def tearDown(self):
    self.alt_driver.stop()

  def test(self):
    self.alt_driver.load_scene("Start", True)
    start_button = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button.click()
    store_button = self.alt_driver.wait_for_object(By.PATH, self.store_button_path, timeout=20)
    store_button.click()
    store_title = self.alt_driver.wait_for_object(By.PATH, self.store_title_path, timeout=20)
    coins_counter = self.alt_driver.wait_for_object(By.PATH, self.coins_counter_path, timeout=20)
    coins_counter.wait_for_component_property("UnityEngine.UI.Text", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    store_title1 = self.alt_driver.wait_for_object(By.PATH, self.store_title_path, timeout=20)
    store_title1.click()
    coins_counter1 = self.alt_driver.wait_for_object(By.PATH, self.coins_counter_path, timeout=20)
    coins_counter1.wait_for_component_property("UnityEngine.UI.Text", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
