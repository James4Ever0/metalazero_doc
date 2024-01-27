#cat gcc_targets.log | xargs -iabc bash -c "amd=\$(which abc); echo \$amd"
cat gcc_targets.log | xargs -iabc bash -c "amd=\$(which abc); unlink \$amd; target=\$(which abc-8); ln -s \$target \$amd"
