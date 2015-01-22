import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import com.datastax.spark.connector._

val conf = new SparkContext(true).set("spark.cassandra.connection.host", "54.67.42.97")
val sc = new SparkContext("spark://54.67.92.5:7077", "all_about_that_database", conf)

val rdd = sc.cassandraTable("all_about_that_database", "guangs_database")
println(rdd.count)
println(rdd.first)

val collection = sc.parallelize(Seq((5, 300, "Frozen Waste"), (6, 450, "Yololand")))
collection.saveToCassandra("all_about_that_database", "guangs_database", SomeColumns("id", "duration", "map_name"))
