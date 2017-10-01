# Contributing to projects in AProjectAMonth initiative

You have found a bug or you have an idea for a cool new feature? Contributing code is a great way to give something back to the open source community. Before you dig right into the code there are a few guidelines that we need contributors to follow so that we can have a chance of keeping on top of things.

Getting Started

<ul>
	<li>Make sure you have a GitHub account.</li>
	<li>If you're planning to implement a new feature it makes sense to discuss you're changes with your pals and developers. This way you can make sure you're not wasting your time on something that isn't considered to be feasible or out of project's scope.</li>
	<li>Clearly describe the issue including steps to reproduce when it is a bug.</li>
	<li>Make sure you fill in the earliest version that you know has the issue.</li>
	<li>Find the corresponding repository on GitHub, fork and check out your forked repository.</li>
</ul>

<h1>Making Changes</h1>

<ul>
	<li>Create a topic branch for your isolated work.</li>
		<ul>
			<li>Usually you should base your branch on the master or trunk branch.</li>
			<li>A good topic branch name can be the issue number plus a keyword, e.g. ISSUE-12-InputStream.</li>
			<li>If you have submitted multiple issues, try to maintain separate branches and pull requests.</li>
		</ul>
	<li>Make commits of logical units.</li>
		<ul>
			<li>Make sure your commit messages are meaningful and in the proper format. Your commit message should contain the key of the issue.</li>
			<li>e.g. ISSUE-12: Close input stream earlier</li>
		</ul>
	<li>Respect the original code style:</li>
		<ul>
			<li>Only use spaces for indentation.</li>
			<li>Create minimal diffs - disable On Save actions like Reformat Source Code or Organize Imports. If you feel the source code should be reformatted create a separate PR for this change first.</li>
			<li>Check for unnecessary whitespace with git diff -- check before committing.</li>
</ul>

<h1>Making Trivial Changes</h1>

For changes of a trivial nature to comments and documentation, it is appropriate to start the first line of a commit with '(doc)' instead of a ticket number.

<h1>Submitting Changes</h1>

<ul>
	<li>Push your changes to a topic branch in your fork of the repository.</li>
	<li>Submit a Pull Request to the corresponding repository in the aprojectamonth organization.</li>
	<li>Verify Files Changed shows only your intended changes and does not include additional files (maybe the virtualenv, .gitignore files etc)</li>
</ul>

