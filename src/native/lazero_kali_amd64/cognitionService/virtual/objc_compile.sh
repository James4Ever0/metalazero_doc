#gcc-8 -o hello -objc cog_core.m 
#gcc-10 -o hello -objc cog_core.m
gcc-10 -o cog_core cog_core.m -I `gnustep-config --variable=GNUSTEP_SYSTEM_HEADERS` \
                       -L `gnustep-config --variable=GNUSTEP_SYSTEM_LIBRARIES` \
                       -lgnustep-base -fconstant-string-class=NSConstantString \
                       -D_NATIVE_OBJC_EXCEPTIONS \
                       -lobjc

