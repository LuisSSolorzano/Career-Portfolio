#include <stdio.h>
#include <conio.h>
#include <Windows.h>

#define MAX_BULLETS_COUNT 100

typedef struct 
{
    int alive;
    char ch;
    int x, y, color;
} 

Object;

Object player = {.alive = 1, .ch = '@', .x = 0, .y = 24, .color = 0x0a};
Object bullets[MAX_BULLETS_COUNT] = {0, };

void erase_object(Object object) 
{
    COORD pos = {.X = object.x,.Y = object.y};

    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0);
    putchar(' ');
}

void draw_object(Object object) 
{
    COORD pos = {.X = object.x, .Y = object.y};

    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), object.color);
    putchar(object.ch);
}

void shoot() 
{
    for (int i = 0; i < MAX_BULLETS_COUNT; ++i) 
    {
        if (!bullets[i].alive) 
	{
            bullets[i].alive = 1;
            bullets[i].ch = '^';
            bullets[i].x = player.x;
            bullets[i].y = player.y;
            bullets[i].color = 0x0f;
            break;
        }
    }
}

void move_bullets() 
{
    for (int i = 0; i < MAX_BULLETS_COUNT; ++i) 
    {
        if (bullets[i].alive) 
	{
            erase_object(bullets[i]);

            if (--bullets[i].y < 0)
                bullets[i].alive = 0;
            else
                draw_object(bullets[i]);
        }
    }
}

int main() {
    int last_bullets_moved = 0;

    srand(GetTickCount());

    while (1) 
    {
        int now = GetTickCount();

        if (_kbhit()) {
            erase_object(player);

            switch (_getch()) 
	    {

            	case 75:

  	              if (--player.x < 0)
        	            player.x = 0;

	              break;

            	case 77:

                	if (++player.x > 78) 
                    		player.x = 78;
                	break;

            case 32:

                shoot();
                break;
            }
        }

        if (now - last_bullets_moved >= 100) 
	{
            move_bullets();
            last_bullets_moved = now;
        }

        draw_object(player);

        Sleep(10);
    }

    return 0;
}