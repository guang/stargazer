name := "SparkCassie"
version := "1.0"
scalaVersion := "2.10.4"
libraryDependencies ++= Seq(
  "com.datastax.spark" %% "spark-cassandra-connector" % "1.2.0-alpha1",
   "org.apache.spark" %% "spark-core" % "1.2.0" % "provided",
   "com.databricks" %% "spark-avro" % "0.1",
   "org.apache.spark" %% "spark-sql" % "1.2.0"
)

assemblyMergeStrategy in assembly := {
    case PathList(ps @ _*) if ps.last endsWith ".RSA" => MergeStrategy.first
    case PathList("META-INF", "mailcap") => MergeStrategy.first
    case PathList("javax", "servlet", xs @ _*)         => MergeStrategy.first
    case PathList(ps @ _*) if ps.last endsWith ".html" => MergeStrategy.first
    case "application.conf"                            => MergeStrategy.concat
    case "unwanted.txt"                                => MergeStrategy.discard
    case PathList("META-INF", "maven","io.netty","netty", xs @ _* ) => MergeStrategy.first
    case PathList("org", "jboss","netty", xs @ _* ) => MergeStrategy.first
    case PathList("META-INF", "maven","org.apache.curator","curator-client", xs @ _* ) => MergeStrategy.first
    case PathList("META-INF", "maven","org.apache.curator","curator-framework", xs @ _* ) => MergeStrategy.first
    case PathList("META-INF", "maven","org.apache.httpcomponents","httpclient", xs @ _* ) => MergeStrategy.first
    case PathList("META-INF", "maven","org.apache.httpcomponents","httpcore", xs @ _* ) => MergeStrategy.first
    case PathList("META-INF", "mimetypes.default") => MergeStrategy.first
    case PathList("com", "esotericsoftware","minlog","Log$Logger.class") => MergeStrategy.first
    case PathList("com", "esotericsoftware","minlog","Log.class") => MergeStrategy.first
    case PathList("com", "google","common","base", xs @ _*) => MergeStrategy.first
    case PathList("javax", "servlet", xs @ _*)         => MergeStrategy.first
    case PathList("javax", "activation", xs @ _*)         => MergeStrategy.first
    case PathList("org", "apache","commons","beanutils", xs @ _*)         => MergeStrategy.first
    case PathList("org", "apache","commons","collections", xs @ _*)         => MergeStrategy.first
    case PathList("org", "apache","commons","logging", xs @ _*)         => MergeStrategy.first
    case PathList("org", "apache","log4j", xs @ _*)         => MergeStrategy.last
    case PathList("org", "apache","jute", xs @ _*)         => MergeStrategy.first
    case PathList("org", "slf4j","impl", xs @ _*)         => MergeStrategy.first
    case x if x.startsWith("plugin.properties") => MergeStrategy.last
    case x if x.startsWith("project.clj") => MergeStrategy.last
    case x =>
       val oldStrategy = (assemblyMergeStrategy in assembly).value
       oldStrategy(x)
}

