App.open("C:\Program Files (x86)\Steam\steamapps\common\BountyOfOne\BountyOfOne.exe")
App.focus("BountyOfOne")
wait("main_menu.png",45)
click("start_button.png")
wait("game_mode.png",45)
click("bounty_hunter_button.png")
wait("player_join_input.png",45)
type(Key.SPACE)
click("character_selection_start_button.png")
wait("loading_screen.png",75)
wait(5)
type(Key.SPACE)
type(Key.SPACE)
type(Key.SPACE)
wait("defeat_screen.png",75)
click("defeat_continue_button.png")
click("defeat_back_menu_button.png")
wait("loading_screen.png",75)
wait(5)
type(Key.SPACE)
type(Key.SPACE)
type(Key.SPACE)
wait("main_menu.png",45)
click("quit_button.png")
