using System;

namespace None
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length >= 1)
            {
                string cmdclass = "None.Commands." + args[0].ToLower();
                if(Type.GetType(cmdclass) != null) {
                    Activator.CreateInstance(Type.GetType(cmdclass), new object[] { args });
                }
            }                       
        }
    }
}
