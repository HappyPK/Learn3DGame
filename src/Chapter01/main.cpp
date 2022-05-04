#include "Game.h"

int main(int argc, char** argv)
{
	Game game;
	bool success = game.Initialize();
	if (success)
	{
		game.Run();
	}
	game.Stop();
	return 0;
}
