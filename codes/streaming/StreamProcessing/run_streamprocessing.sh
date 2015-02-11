sudo -u hdfs spark-submit --class StreamProcessing --master local[2] --jars target/scala-2.10/StreamProcessing-assembly-1.0.jar target/scala-2.10/streamprocessing_2.10-1.0.jar
