Learning Appp
==========================

For learning automated mobile testing

### Appium



#### Part 1
Download latest node and npm tools MSI (version >= 6.0) https://nodejs.org/download/release/v6.3.0/node-v6.3.0-x64.msi 
The npm and nodejs paths should be in your PATH environment variable. (by default they are)
Open admin cmd prompt
Run the command npm install -g appium which will install Appium from NPM
run appium from the prompt.
Download and install https://github.com/appium/appium-desktop/releases

#### Part 2

 1. Download the latest Java JDK [here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (accept the license agreement first). Set 'JAVA_HOME' to be your JDK path. The `bin` in that directory should be added to your PATH variable.
   2. Install the [Android SDK](http://developer.android.com/sdk/index.html). Set the `ANDROID_HOME` environment variable to be your Android SDK path and add the `tools` and `platform-tools` folders to your PATH variable.
   3. Install [Apache Ant](http://ant.apache.org/bindownload.cgi) or use the one that comes with the Android Windows SDK in the eclipse\plugins folder. Be sure to add the folder containing Ant to your PATH variable.
   4. Install [Apache Maven](http://maven.apache.org/download.cgi) and set the M2HOME and M2 environment variables. Set `M2_HOME` to the directory maven is installed in, and set `M2` to the `bin` in that directory. Add the path you used for `M2` to your PATH.
   5. To run tests on Windows, you will need to have the Android Emulator booted or an Android Device connected that is running an AVD with API Level 17 or greater. Then run Appium on the command line (via the `appium` command)
   6. Your test script should ensure that the `platformVersion` capability corresponds to the emulator or device version you are testing, and that the `app` capability is an absolute path to the .apk file of the Android app.

#### License

~~~~
Do what you want with it
~~~~
