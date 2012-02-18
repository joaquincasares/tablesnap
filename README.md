Tablesnap
=========

This Fork
---------

* Creates the bucket if not yet created.
* Adds download capabilities.
* Uses the AMI launch index within the EC2 bucket instead of the hostname, by default.
* Allows for a tablesnap.conf file to house all the command line arguments.

Theory of Operation
-------------------

Tablesnap is a script that uses inotify to monitor a directory for `IN_MOVED_TO`
events and reacts to them by spawning a new thread to upload that file to
Amazon S3, along with a JSON-formatted list of what other files were in the
directory at the time of the copy.

When running a Cassandra cluster, this behavior can be quite useful as it
allows for automated point-in-time backups of SSTables. Theoretically,
tablesnap should work for any application where files are written to some
temporary location, then moved into their final location once the data is
written to disk. Tablesnap also makes the assumption that files are immutable
once written.

Installation
------------

Run `python setup.py install`.

Configuration
-------------

Configurations happen in the command line or via
`$TABLESNAP_CONF`,
`./tablesnap.conf`,
`~/.tablesnap.conf`, or
`/etc/tablesnap/tablesnap.conf`.

    Usage: tablesnap [options] <bucket> <path> [...]
    Options:
      -h, --help            show this help message and exit
      -k AWS_KEY, --aws-key=AWS_KEY
      -s AWS_SECRET, --aws-secret=AWS_SECRET
      -r, --recursive       Recursively watch the given path(s)s for new SSTables
      -a, --auto-add        Automatically start watching new subdirectories within path(s)
      -B, --backup          Backup existing SSTables to S3 if they're not already there
      -D, --download        Download existing SSTables on S3 to this EC2 instance


For example:

    $ tablesnap -k AAAAAAAAAAAAAAAA -s BBBBBBBBBBBBBBBB me.synack.sstables /var/lib/cassandra/data/GiantKeyspace

This would cause tablesnap to use the given Amazon Web Services credentials to
backup the SSTables for my `GiantKeyspace` to the S3 bucket named
`me.synack.sstables`.

    $ tablesnap -k AAAAAAAAAAAAAAAA -s BBBBBBBBBBBBBBBB -D me.synack.sstables /tmp

This would cause tablesnap to downlad the uploaded files into the `/tmp` directory.
Using `/` as the path would download the files to the same directory.

Questions, Comments, and Help
-----------------------------
The fine folks in `#cassandra-ops` on `irc.freenode.net` are an excellent
resource for getting tablesnap up and running, and also for solving more
general Cassandra issues.
