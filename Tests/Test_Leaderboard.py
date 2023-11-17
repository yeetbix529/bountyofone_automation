App.open("C:\Program Files (x86)\Steam\steamapps\common\BountyOfOne\BountyOfOne.exe")
App.focus("BountyOfOne")

wait("main_menu.png",45)
click("leaderboard_button.png")
wait("leaderboard.png",45)
click("leaderboard_back_to_menu.png")
wait("main_menu.png",45)
click("quit_button.png")