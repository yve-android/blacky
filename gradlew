#!/bin/sh

##############################################################################
# Gradle startup script for UN*X
##############################################################################

# Resolve links: $0 may be a link
APP_HOME="${0%/*}"
cd "$APP_HOME" || exit

exec java -classpath "$APP_HOME/gradle/wrapper/gradle-wrapper.jar" org.gradle.wrapper.GradleWrapperMain "$@"
