FROM maven:3.9.8-eclipse-temurin-21

COPY src /usr/src/app/src
COPY pom.xml /usr/src/app
RUN mvn -f /usr/src/app/pom.xml package


EXPOSE 80
CMD ["java","-jar","/usr/src/app/target/app.jar"]