#include <iostream>
#include <conio.h>   // 用于获取键盘输入
#include <windows.h> // 用于控制命令行窗口
#include <stddef.h>

using namespace std;

const int width = 20;  // 游戏区域宽度
const int height = 20; // 游戏区域高度

int x, y;                   // 蛇头的坐标
int fruitX, fruitY;         // 食物的坐标
int tailX[100], tailY[100]; // 蛇尾的坐标
int nTail;                  // 蛇的长度
enum eDirection
{
    STOP = 0,
    LEFT,
    RIGHT,
    UP,
    DOWN
};              // 枚举类型表示方向
eDirection dir; // 当前蛇头移动方向
bool gameOver;  // 游戏结束标志

void Setup()
{
    gameOver = false;
    dir = STOP;    // 初始时静止不动
    x = width / 2; // 蛇头初始坐标位于游戏区域中心
    y = height / 2;
    fruitX = rand() % width; // 随机生成食物坐标
    fruitY = rand() % height;
    nTail = 0; // 初始时蛇的长度为零
}

void Draw()
{
    system("cls");                      // 清屏
    for (int i = 0; i < width + 2; i++) // 绘制游戏区域上边界
        cout << "#";
    cout << endl;
    for (int i = 0; i < height; i++)
    { // 绘制游戏区域
        for (int j = 0; j < width; j++)
        {
            if (j == 0) // 绘制游戏区域左边界
                cout << "#";
            if (i == y && j == x) // 绘制蛇头
                cout << "O";
            else if (i == fruitY && j == fruitX) // 绘制食物
                cout << "F";
            else
            {
                bool printTail = false; // 判断该点是否是蛇身
                for (int k = 0; k < nTail; k++)
                {
                    if (tailX[k] == j && tailY[k] == i)
                    {
                        cout << "o";
                        printTail = true;
                    }
                }
                if (!printTail) // 如果不是蛇身则输出空格
                    cout << " ";
            }
            if (j == width - 1) // 绘制游戏区域右边界
                cout << "#";
        }
        cout << endl;
    }
    for (int i = 0; i < width + 2; i++) // 绘制游戏区域下边界
        cout << "#";
    cout << endl;
}

void Input()
{
    if (_kbhit())
    { // 如果有键盘输入
        switch (_getch())
        { // 判断输入的键盘按键
        case 'a':
            dir = LEFT;
            break;
        case 'd':
            dir = RIGHT;
            break;
        case 'w':
            dir = UP;
            break;
        case 's':
            dir = DOWN;
            break;
        case 'x':
            gameOver = true;
            break;
        }
    }
}

void Logic()
{
    int prevX = tailX[0], prevY = tailY[0]; // 记录蛇尾的位置，用于后面的移动操作
    int prev2X, prev2Y;
    tailX[0] = x; // 蛇尾跟随蛇头移动
    tailY[0] = y;
    for (int i = 1; i < nTail; i++)
    { // 蛇身跟随蛇尾移动
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }
    switch (dir)
    { // 根据当前方向移动蛇头
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UP:
        y--;
        break;
    case DOWN:
        y++;
        break;
    default:
        break;
    }
    if (x >= width) // 处理边界情况，如果蛇头碰到边界则游戏结束
        x = 0;
    else if (x < 0)
        x = width - 1;
    if (y >= height)
        y = 0;
    else if (y < 0)
        y = height - 1;
    for (int i = 0; i < nTail; i++) // 如果蛇头碰到蛇身则游戏结束
        if (tailX[i] == x && tailY[i] == y)
            gameOver = true;
    if (x == fruitX && y == fruitY)
    { // 如果蛇头碰到食物，则食物被吃掉，蛇长一节
        nTail++;
        fruitX = rand() % width; // 随机生成新的食物坐标
        fruitY = rand() % height;
    }
}

int main()
{
    Setup();
    while (!gameOver)
    { // 游戏主循环
        Draw();
        Input();
        Logic();
        Sleep(100); // 控制蛇的移动速度，毫秒级别
    }
    return 0;
}
