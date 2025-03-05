
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  char_name_path = "/UICamera/Loadout/CharZone/CharName"
  image_path = "/UICamera/Loadout/ThemeZone/Image"
  theme_name_path = "/UICamera/Loadout/ThemeZone/Image/ThemeName"
  start_button_path1 = "/UICamera/Loadout/StartButton"
  text_path = "/UICamera/Loadout/StartButton/Text"
  open_leaderboard_path = "/UICamera/Loadout/OpenLeaderboard"
  text_path1 = "/UICamera/Loadout/OpenLeaderboard/Text"
  store_button_path = "/UICamera/Loadout/StoreButton"
  text_path2 = "/UICamera/Loadout/StoreButton/Text"
  mission_button_path = "/UICamera/Loadout/MissionButton"
  text_path3 = "/UICamera/Loadout/MissionButton/Text"
  setting_button_path = "/UICamera/Loadout/SettingButton"
  text_path4 = "/UICamera/Loadout/SettingButton/Text"

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
    char_name = self.alt_driver.wait_for_object(By.PATH, self.char_name_path, timeout=20)
    image = self.alt_driver.wait_for_object(By.PATH, self.image_path, timeout=20)
    theme_name = self.alt_driver.wait_for_object(By.PATH, self.theme_name_path, timeout=20)
    start_button1 = self.alt_driver.wait_for_object(By.PATH, self.start_button_path1, timeout=20)
    start_button1.wait_for_component_property("UnityEngine.UI.Button", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    text = self.alt_driver.wait_for_object(By.PATH, self.text_path, timeout=20)
    open_leaderboard = self.alt_driver.wait_for_object(By.PATH, self.open_leaderboard_path, timeout=20)
    open_leaderboard.wait_for_component_property("UnityEngine.UI.Button", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    text1 = self.alt_driver.wait_for_object(By.PATH, self.text_path1, timeout=20)
    store_button = self.alt_driver.wait_for_object(By.PATH, self.store_button_path, timeout=20)
    store_button.wait_for_component_property("UnityEngine.UI.Button", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    text2 = self.alt_driver.wait_for_object(By.PATH, self.text_path2, timeout=20)
    mission_button = self.alt_driver.wait_for_object(By.PATH, self.mission_button_path, timeout=20)
    mission_button.wait_for_component_property("UnityEngine.UI.Button", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    text3 = self.alt_driver.wait_for_object(By.PATH, self.text_path3, timeout=20)
    setting_button = self.alt_driver.wait_for_object(By.PATH, self.setting_button_path, timeout=20)
    setting_button.wait_for_component_property("UnityEngine.UI.Button", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    text4 = self.alt_driver.wait_for_object(By.PATH, self.text_path4, timeout=20)
