﻿using OpenCorepiAndBypass.src;
using System;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Resources;
using System.Threading;

namespace OpenCorepiAndBypass
{



    class Program
    {
        const string VERSION = "v0.0.3";

        /// <summary>
        /// 绘制版本启动
        /// </summary>
        private static void DrawVersion()
        {
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("╔══════════════════════════════════════════════════════════╗");
            Console.WriteLine("║                        AutoOpenCAK                       ║");
            Console.WriteLine("║                                                          ║");
            Console.Write("║                 ");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write(VERSION);
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.Write(" : ");
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Write("原神");
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.Write(",");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("启动");
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.Write("!!!!");
            Console.WriteLine("                   ║");
            Console.WriteLine("║                      绕过米哈游检测                      ║");
            Console.WriteLine("║                                                          ║");
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("╚══════════════════════════════════════════════════════════╝");
            Console.ResetColor();
        }

        /// <summary>
        /// 获取资源管理器
        /// </summary>
        /// <returns>资源管理器</returns>
        private static ResourceManager GetResourceManager()
        {

            bool loop = true;

            // 使用while循环来重复执行以下代码，直到loop为false
            while (loop)
            {
                // 输出语言选择菜单
                Console.ForegroundColor = ConsoleColor.DarkCyan;
                Console.WriteLine("请选择语言：| Please select a language:");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("1. 中文 | 1. Chinese");
                Console.WriteLine("2. 英文 | 2. English");
                Console.ResetColor();

                // 读取用户输入的选择
                string choice = Console.ReadLine();

                // 使用switch语句来根据选择设置语言和退出循环
                switch (choice)
                {
                    case "1":
                        Thread.CurrentThread.CurrentUICulture = new CultureInfo("zh-CN");
                        loop = false; // 设置loop为false，退出循环
                        break;
                    case "2":
                        Thread.CurrentThread.CurrentUICulture = new CultureInfo("en");
                        loop = false; // 设置loop为false，退出循环
                        break;
                    default:
                        Console.WriteLine("无效选择！| Invalid selection!");
                        break;
                }
            }


            // 创建资源管理器对象
            ResourceManager rm = new System.Resources.ResourceManager("OpenCorepiAndBypass.Properties.Strings", Assembly.GetExecutingAssembly());


            return rm;
        }


        static void Main(string[] args)
        {
            DrawVersion();

            ResourceManager rm = GetResourceManager();

            //TODO
            //判断是否存在配置文件 初始化配置待完成

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            //读取配置文件
            IniFile ini = new IniFile(@Environment.CurrentDirectory + @"\config.ini");
            if (ini != null)
            {
                Console.WriteLine(rm.GetString("Conf_Success"));
            }
            //账号切换器
            string genshinAccount = ini.ReadValue("Settings", "GenshinAccount");
            if (genshinAccount.Contains("true"))
            {
                Console.WriteLine(rm.GetString("Change_message"));
                string genshinAccountPath = ini.ReadValue("Settings", "GenshinAccountPath");

                Console.WriteLine(rm.GetString("Load_Path"));

                FileUtils.OpenFile(@genshinAccountPath);

                Thread.Sleep(5000);
            }
            else
            {
                Console.WriteLine(rm.GetString("Cancle_Open") + rm.GetString("AccountSwitcher"));
            }

            Console.WriteLine("");

            //3dm
            string ThreeDM = ini.ReadValue("Settings", "ThreeDM");
            if (ThreeDM.Contains("true"))
            {
                Console.WriteLine(rm.GetString("Open_Agree") + "3dm");
                string ThreeDMPath = ini.ReadValue("Settings", "ThreeDMPath");

                Console.WriteLine(rm.GetString("Load_Path"));
                FileUtils.OpenFile(ThreeDMPath);

                // 暂停1秒
                Thread.Sleep(2000);
            }
            else
            {
                Console.WriteLine(rm.GetString("Cancle_Open") + "3dm");
            }

            Console.WriteLine("");


            //执行过检测
            string ByPass = ini.ReadValue("Settings", "ByPass");
            if (ByPass.Contains("true"))
            {
                Console.WriteLine(rm.GetString("Open_Agree") + rm.GetString("Bypass_Name"));


                string GamePath = ini.ReadValue("Settings", "GamePath") + @"\";
                Console.WriteLine(GamePath);


                //判断文件夹是否存在,不存在报错并且重新选择
                if (!Directory.Exists(GamePath))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("游戏路径不存在，请重新选择路径。");
                    // 重新选择路径的代码
                    GamePath = FileUtils.GetFolderPath("选择游戏路径文件夹,选错可能导致游戏无法运行 文件夹名称为:Genshin Impact Game");
                    if (GamePath.Length <= 3)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("选择的路径长度不对");
                        Console.Read();
                        Environment.Exit(1);
                    }
                }
                Console.ForegroundColor = ConsoleColor.DarkGreen;

                Console.WriteLine(rm.GetString("Bypass_Message"));
                Console.WriteLine("");
                Console.WriteLine(rm.GetString("HoYoKProtect_no_exist"));


                FileUtils.ChangeFileName(@GamePath + "HoYoKProtect.sys", @GamePath + "HoYoKProtect.sys.bak", "HoYoKProtect.sys");
                FileUtils.ChangeFileName(@GamePath + "mhypbase.dll", @GamePath + "mhypbase.dll.bak", "mhypbase.dll");
                FileUtils.ChangeFileName(@GamePath + "mhyprot3.Sys", @GamePath + "mhyprot3.Sys.bak", "mhyprot3.Sys");



                // 暂停1秒
                Thread.Sleep(2000);

            }
            Console.WriteLine("");
            //执行注入

            string Injector = ini.ReadValue("Settings", "Injector");
            if (Injector.Contains("true"))
            {

                Console.WriteLine(rm.GetString("Open_Agree") + rm.GetString("Injector"));
                string InjectorPath = ini.ReadValue("Settings", "InjectorPath");
                FileUtils.OpenFile(InjectorPath);

                // 暂停15秒
                Console.WriteLine(rm.GetString("Wait_Injector_Time"));
                Thread.Sleep(20000);
            }


            //取消bypass
            if (ByPass.Contains("true"))
            {
                string GamePath = ini.ReadValue("Settings", "GamePath") + @"\";

                Console.WriteLine(rm.GetString("Cahcoe_Bypass_Message"));

                FileUtils.ChangeFileName(@GamePath + "HoYoKProtect.sys.bak", @GamePath + "HoYoKProtect.sys", "HoYoKProtect.sys.bak");
                FileUtils.ChangeFileName(@GamePath + "mhypbase.dll.bak", @GamePath + "mhypbase.dll", "mhypbase.dll.bak");
                FileUtils.ChangeFileName(@GamePath + "mhyprot3.Sys.bak", @GamePath + "mhyprot3.Sys", "mhyprot3.Sys.bak");


                // 暂停1秒
                Thread.Sleep(2000);
                Console.WriteLine("");
            }

            //CB运行
            string CB = ini.ReadValue("Settings", "CB");
            if (CB.Contains("true"))
            {
                string CBPath = ini.ReadValue("Settings", "CBPath");
                FileUtils.OpenFile(CBPath);
                Console.WriteLine(rm.GetString("Open_Agree") + "CB");

            }

            Console.WriteLine("");

            Console.ForegroundColor = ConsoleColor.Red;

            Console.WriteLine(rm.GetString("Exit_Message"));

            Console.Read();
            Console.Read();
        }


    }
}
