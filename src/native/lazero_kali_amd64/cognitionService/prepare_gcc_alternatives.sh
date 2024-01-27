#cat gcc_targets.log | xargs -iabc bash -c "amd=\$(which abc); echo \$amd"
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 5
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 4
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 3

update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 5
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 4
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 3
