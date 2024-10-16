'''
ENVIRONMENT VARIABLES AND YOU

    SYNTAX
            EV's are set using the following syntax: <variable name>=<value>
                - variable names tend to be all caps
                - the equal sign does not have spaces around it (the shell will throw an error if there are, because it will think the variable name is a command)
            Important symbols:
                $     Used when calling a variable
                ''    String literal. does not interpolate anything between apostrophes
                ""    Inner variable interpolation
                >>    Redirection operator - used to append text to a file. If a target doesn't exist, it will be created.
                >     Redirection operator - used to overwrite a file. If a target doesn't exist, it will be created.
            Example: 
                $ MESSAGE1="This is message 1."
                $ MESSAGE2="This is message 2."
                $ MESSAGE="$MESSAGE1 $MESSAGE2"
                $ echo $MESSAGE
                This is message 1. This is message 2.
        
    PERSISTENCE
            Environment variables (EV) defined on the command prompt last for the duration of the session
                - If the EV is defined immediately before a command on the same line, the EV returns to its previous value (if it already existed) or is deleted (if it didn't exist
                before) after the command is run
                - If a variable is set on the same line that it is invoked, it will not be invoked because the  invocation is evaluated before setting occurs

    ENVIRONMENT FILES
            For more persistent variables (variables that exist between sessions), variables can be added to environment files that are automatically run when a terminal window is opened. 
                - examples of environment files are .bashrc, .bash_profile, .zshrc, and .zprofile. The environment file name depends on the flavor of shell you are using (bash, zsh, etc.)
                - syntax inside the . (hidden) files goes like this: 
                    Bash: export <variable_name>=<value>
                - special characters
                    \h     Hostname
                    \u     User name
                    \w     Current directory
                    \w     Basename of current directory
                    \d     Current date
                    \n     Newline
            .bashrc, .zshrc, .bash_profile, and .zprofile files are automatically run when opening a new terminal session. 
            To manually run these files (and enable their settings), use the source command: source ~/.bashrc

    PATH
            All shell commands are executable files that live in directories. The PATH variable contains all the directories (paths) that the shell program will search for a command.
            The shell searches these paths sequentially.

'''