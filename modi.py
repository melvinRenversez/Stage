old_email = bytes([107,115,100,106,97,112,111,110,64,103,109,97,105,108,46,99,111,109])
new_email = bytes([109,101,108,118,105,110,114,101,110,118,101,114,115,101,122,48,48,51,64,103,109,97,105,108,46,99,111,109])
new_name = bytes([109,101,108,118,105,110,82,101,110,118,101,114,115,101,122])

if commit.author_email == old_email:
    commit.author_name = new_name
    commit.author_email = new_email

if commit.committer_email == old_email:
    commit.committer_name = new_name
    commit.committer_email = new_email