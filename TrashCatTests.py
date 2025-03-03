
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  mission_button_path = "/UICamera/Loadout/MissionButton"
  close_button_path = "/UICamera/Loadout/MissionPopup/MissionBackground/CloseButton"
  start_button_path1 = "/UICamera/Loadout/StartButton"
  game_over_path = "/UICamera/Game/DeathPopup/GameOver"
  loadout_path = "/UICamera/GameOver/Loadout"
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
    start_button = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button.click()
    mission_button = self.alt_driver.wait_for_object(By.PATH, self.mission_button_path, timeout=20)
    mission_button.click()
    close_button = self.alt_driver.wait_for_object(By.PATH, self.close_button_path, timeout=20)
    close_button.click()
    self.alt_driver.load_scene("Start", True)
    start_button1 = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button1.click()
    start_button2 = self.alt_driver.wait_for_object(By.PATH, self.start_button_path1, timeout=20)
    start_button2.click()
    game_over = self.alt_driver.wait_for_object(By.PATH, self.game_over_path, timeout=20)
    game_over.click()
    loadout = self.alt_driver.wait_for_object(By.PATH, self.loadout_path, timeout=20)
    loadout.click()
    self.alt_driver.load_scene("Start", True)
    start_button3 = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button3.click()
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
