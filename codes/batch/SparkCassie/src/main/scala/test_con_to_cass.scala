import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
import com.datastax.spark.connector._
import com.databricks.spark.avro._

object SparkCassie {
  def main(args: Array[String]) {
    val conf = new SparkConf(true).set("spark.cassandra.connection.host", "54.67.42.97")

    val sc = new SparkContext(conf)
    val cassie = sc.cassandraTable("matches_simple", "map_duration_over_time")
    // val cassie = sc.cassandraTable("matches_simple", "yolo_try")

    // load avro files and save as table
    val sqlContext = new SQLContext(sc)
    val matches_simple = sqlContext.avroFile("/matches_5673896_simple.avro")
    matches_simple.registerTempTable("simple")

    // make queries get data
    // val results = sqlContext.sql("insert into map_duration_over_time.matches_simple select match_id, ended_at, map_name, duration_seconds from simple")
    val query_results  = sqlContext.sql("select match_id, ended_at, map_name, duration_seconds from simple")
    val results = query_results.map(row => (row.getInt(0), row.getFloat(1), row.getString(2), row.getInt(3)))
    results.saveToCassandra("matches_simple", "map_duration_over_time", SomeColumns("match_id", "ended_at", "map_name", "duration_seconds"))
  }
}
