#pragma once
#include "SDL.h"

struct Vector2
{
	float x;
	float y;
};

class Game
{
public:
	Game();

	bool Initialize();
	void Run();
	void Stop();

private:
	void ProcessInput();
	void Update();
	void GenerateOutput();

private:
	// Window created by SDL
	SDL_Window* mWindow;
	// Renderer for 2D drawing
	SDL_Renderer* mRenderer;
	// Number of ticks since start of game
	Uint32 mTicksCount;
	// Game should continue to run
	bool mIsRunning;

private:
	// Pong specific
	// Direction of paddle
	int mPaddleDir;
	// Position of paddle
	Vector2 mPaddlePos;
	// Position of ball
	Vector2 mBallPos;
	// Velocity of ball
	Vector2 mBallVel;
};