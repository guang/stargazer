import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import com.datastax.spark.connector._

object SparkCassie {
	def main(args: Array[String]) {
		val conf = new SparkConf(true).set("spark.cassandra.connection.host", "54.67.42.97")
		//val sc = new SparkContext("spark://54.67.92.5:7077", "all_about_that_database", conf)
		
		val sc = new SparkContext(conf)
		val rdd = sc.cassandraTable("all_about_that_database", "map_duration")
		
		val raw = sc.textFile("/guang/dummy.csv").map(line => line.split(","))
    val avg_duration = raw.map(line => (line(5), line(10).toInt)).reduceByKey(_+_/2)


		avg_duration.saveToCassandra("all_about_that_database", "map_duration", SomeColumns("map_name", "duration"))
	}
}	
