using System;
namespace None.Commands
{class powershell
{public powershell(string[] args)
{
            string command = "";
            string enccommand = "";
            for(int idx = 0; idx < args.Length; idx++)
            {
                string arg = args[idx];
                string cmd = "";
                if(arg.Length >= 2)
                {
                    cmd = arg.Substring(0, 2);
                }
                else
                {
                    cmd = arg;
                }
                switch(cmd)
                {
                    case "-c":
                        if(idx + 1 < args.Length)
                        {
                            command = args[idx + 1];
                        }
                        break;
                    case "-e":
                        if (idx + 1 < args.Length)
                        {
                            enccommand = args[idx + 1];
                        }
                        break;
                }
            }
            if(command != "" && enccommand != "")
            {
                ConsoleColor curcolor = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(@"Parameter cannot be processed because the parameter name 'e' is ambiguous. Possible matches include: -ErrorAction 
-ErrorVariable.
At line:1 char:10
    + CategoryInfo          : InvalidArgument: (:), ParameterBindingException
    + FullyQualifiedErrorId : AmbiguousParameter,Microsoft.PowerShell.Commands.GetDateCommand

");
                Console.ForegroundColor = curcolor;
            }
            else
            {
                if(command != "")
                {
                    switch(command.ToLower())
                    {
                        case "get-date":
                            Console.WriteLine("");
                            Console.WriteLine(DateTime.Now.ToString("dddd, MMMM d, yyyy hh:mm:ss tt"));
                            Console.WriteLine("");
                            break;
                        default:
                            string[] cmdparts = command.Split(' ');
                            ConsoleColor curcolor = Console.ForegroundColor;
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine(@"{0} : The term '{0}' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ {0}
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (notacmd:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException", cmdparts[0]);
                            Console.ForegroundColor = curcolor;
                            break;

                    }
                }
            }
        
}}}