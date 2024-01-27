#!/bin/bash
# is this not for aarch64? it's slow anyway.
bin/x86_64/nsjail -Mo --chroot root/ --rw  --disable_clone_newns -- $(which bash) -c "cd $PWD && bash"
