import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
import com.datastax.spark.connector._
import com.databricks.spark.avro._

object SparkCassie {
  def main(args: Array[String]) {
    val conf = new SparkConf(true).set("spark.cassandra.connection.host", "54.67.42.97")
    //val sc = new SparkContext("spark://54.67.92.5:7077", "all_about_that_database", conf)

    val sc = new SparkContext(conf)
    val rdd = sc.cassandraTable("matches_simple", "map_duration_over_time")

    val sqlContext = new SQLContext(sc)
    val matches_simple = sqlContext.avroFile("/matches_5673896_simple.avro")
    matches_simple.registerTempTable("simple")

    val results = sqlContext.sql("select match_id, ended_at, map_name, duration_seconds from simple")

    results.saveToCassandra("matches_simple", "map_duration_over_time", SomeColumns("match_id", "ended_at", "map_name", "duration_seconds"))
  }
}
