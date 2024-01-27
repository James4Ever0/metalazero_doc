#!/bin/bash
sudo rm -f ramdisk/*
sudo find -P ramdisk/ | xargs sudo unlink
sudo rm -rf ramdisk/*
