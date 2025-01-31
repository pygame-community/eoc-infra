NOTE: I use colons as a delimiter between GH users and one of ther repositories, e.g. `ddorn:eoc-dev`.

This proposal separates WeeklyChallenges ( <https://github.com/pygame-community/LegacyWeeklyChallenges> ) into 6 separate repositories and rebrands it as Era of Challenges ( <https://github.com/pygame-community/EraOfChallenges> ).


## Delegating the "development repository" responsibilty.
`pygame-community:LegacyWeeklyChallenges` should no longer be the repository to fork to participate in era of challenges.

Instead, a new GitHub repository should be created called `pygame-community:eoc-dev` . This allows people to simply instantiate a repository for working on challenges by forking it, which would come preconfigured with everything needed to work on specific challenges. As time passes, participants will be able to join new challenges by fetching new branches for those challenges. EOC challenge branches would be of the form `eoc<xxx>_challenge_name/template`  (`xxx` will be a three digit number with leading zeros if necessary, and can be continually expanded to more digits as needed), e.g. `eoc006_platformer/template`. These templates would be provided by challenge creators.

To start working on a challenge inside a `<username>:eoc-dev` fork (e.g. `ddorn:eoc-dev`), a user would need to fetch the newest template branches from `eoc-dev`, e.g. `git fetch upstream`  (`upstream` is `pygame-community:eoc-dev`, while `origin` would be the fork of the form `<username>:eoc-dev`). They would then check-out their target template branch and make a new branch from it to work with, e.g.:

```sh
git remote add upstream "https://github.com/pygame-community/eoc-dev"
git fetch upstream
git switch eoc006_platformer/template
git switch -c eoc006_platformer/ddorn # will create a new branch and switch to it
``` 

The overall structure for a template branch would be as follows:

```
 /
  ┣ eoc<xxx>_challenge_name/ # the source code folder (mandatory)
  ┃  ┗ __init__.py # The only permitted entry point
  ┃  ┣ ...
  ┣ challenge.json
  ┣ requirements.txt
  ┗ README.md             # contains challenge instructions
```

 
## Delegating the "submission repository" responsibilty.
`pygame-community:LegacyWeeklyChallenges` should no longer be the repository to use for challenge submissions.

Instead, submission should occur by opening PRs to `pygame-community:eoc-submissions` from a fork of the form `<username>:eoc-dev`, tagged with their challenge number as a label and submitted in a timely manner. Submissions would introduce branches of the form `eoc<xxx>_challenge_name/<username>` (e.g. `eoc006_platformer/ddorn`)  into the `eoc-submissions` repository.
 
## Delegating the "Era of Challenges Library" responsibilty.
`pygame-community:LegacyWeeklyChallenges` should no longer be the repository that contains `wclib`.  Instead, a new GitHub monorepo should be created called [`pygame-community:eoc-infra`](https://github.com/pygame-community/eoc-infra) and [`pygame-community:eoc.challenges`](https://github.com/pygame-community/eoc.challenges). The former will be a monorepo containing a helper CLI tool for submission called `eoc` and a library for managing challenge-agnostic infrastructure called `eoclib`, while the latter will host challenge-specific helper tools and assets.

`eoc.challenges` will be another [namespace package](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/), whose contained modules derive from `eoclib` in [`pygame-community:eoc-infra`](https://github.com/pygame-community/eoc-infra), and host the assets for every challenge (using a `MANIFEST.in` file and similar mechanisms: https://python-packaging.readthedocs.io/en/latest/non-code-files.html, https://setuptools.pypa.io/en/stable/userguide/datafiles.html#package-data),  there will be challenge-specific editions of `eoc.libs.core` in their own branches. Each of those branches would be of the form `eoc<xxx>_challenge_name` (same as the challenge name). Installing them would look like this: `pip install "eoc.challenges.eoc006_platformer @ git+https://github.com/pygame-community/eoc.challenges@eoc006_platformer.git"` . These strings will be exposed inside template branches of `pygame-community:eoc-dev` in `requirements.txt` files.

Era of Challenges submissions should import these editions as follows: `import eoc.challenges.eoc006_platformer as eoc006`. `eoc006.assets.audio` and `eoc006.assets.images` would both expose string constants that map to the assets, e.g. `eoc006.assets.images.PLAYER`.

## Delegating the "Era of Challenges Client" responsibilty.
`pygame-community:EraOfChallenges` should only act as a "player" for playing Weekly Challenges. To avoid people having to download `pygame-community:eoc-submissions` or anything similar, the program would download challenge files on demand from GitHub (`https://github.com/pygame-community/pygame-ce/archive/refs/heads/eoc007_platformer/ddorn.zip`), and keep them around in a locally generated cache of the form `.eoccache/eoc<xxx>_challenge_name/<username>/*` .

To make this work, 3 requirements have to be met:

1. There needs to be a branch in `pygame-community:eoc-submissions` called `eoc<xxx>_challenge_name/info` containing a `challengeinfo.json` file describing a challenge and what achievements it supports.

2. Each challenge submission branch of a participant (`eoc<xxx>_challenge_name/<username>`) will need a top level `challenge.json` file containing any important challenge metadata (e.g. submitter usernames). It will be generated by a script (e.g. `python3 -m eoc submit`) that triggers an interactive CLI prompt, asking questions relevant to the needed `challenge.json` fields (supported achievements would be looked up inside `eoc<xxx>_challenge_name/info`, e.g. `https://cdn.jsdelivr.net/gh/pygame-community/eoc-submissions@eoc006_platformer/info/challengeinfo.json`), as well as prompting for whether repetitive data should be stored inside of Git's repository-level config data if not already present (stored as `git config --local user.name <username>` / `git config --local user.discord_username <Discord username>`, read as `git config --local --get user.name <username>` / `git config --local --get user.discord_username <discord_username>`).

    An initial `challenge.json` could look like this:
    
    ```jsonc
    {
        "github_username": "...", // (required)
        "discord_username": "...", // (optional)
        "display_name": "...", // A preferred display name (optional)
        "achievements": [
           // achievement field names
        ],
    }
    ```
    and a completed one like this:
    ```jsonc
    {
        "github_username": "ddorn",
        "discord_username": "@CozyFractal",
        "display_name": "Cozy",
        "achievements": [
            "casual",
            "ambitious"
        ]
    }
    ```

3. Each challenge must have a corresponding branch in `pygame-community/eoc-submissions` called `eoc<xxx>_challenge_name/submitters`, which itself contains a `submitters.txt` file listing up GitHub usernames of users who submitted, in order to build links like `https://github.com/pygame-community/eoc-submissions/archive/refs/heads/eoc007_platformer/ddorn.zip` to download a user's submission code and `challenge.json`, with `eoc<xxx>_challenge_name/__init__.py` serving as the entry point for `EraOfChallenges` to load a user's submission as a module at runtime.

All in all, these changes would lead to a far more scalable future for Era of Challenges.
