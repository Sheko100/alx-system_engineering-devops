# Project about using sftp to transfer files

## Connecting to the sandbox (host)

To connect through **sftp**, we run the following command:

`sftp <username>@<host>`

where `<username>` is our **username** and `<host>` is our **destination host**

After that we type our **password** and press **enter/return** to get in

Now we are in the **root** `/` of the host

## Navigating to the destination

Before sending any files, we need to go to the destination that we need those files to be sent

We can do that normally by using the `cd` command, so for example we can go to the `/root/alx-system_engineering-devops/command_line_for_the_win` directory by running the following command:

`cd /root/alx-system_engineering-devops/command_line_for_the_win`

But that's for the remote host, then how do we navigate locally?

We can use any command locally by **prefixing** the command with `l` the starting character of **local**, so we can know where we are locally by running the following command:

`lpwd`

So we need to use `lcd` command to go to the directory where we **store** the files we want to send, so we can do that by the running the following command:

`lcd <dist-dir>`

## Transferring the files

As all is good so far and we are in the desired directories in both remotly and locally, then we can start transferring

To transfer from **local** to **remote**, we can use the following command:

`put <file-name>`

for example:

`put 0-first_9_tasks.png`

To tranfer from **remote** to **local**, we can use the following command:

`get <file-name>`

for example:

`get 0-first_9_tasks.png`
