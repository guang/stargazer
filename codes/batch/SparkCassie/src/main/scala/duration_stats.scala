import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
import com.datastax.spark.connector._
import com.databricks.spark.avro._

object SparkCassie {
  def main(args: Array[String]) {
    // -- Initialization --
    val conf = new SparkConf(true).set("spark.cassandra.connection.host", "54.67.42.97")
    val sc = new SparkContext(conf)

    // load avro files and save as table
    val sqlContext = new SQLContext(sc)
    val matches_simple = sqlContext.avroFile("/data/matches_5673896_simple.avro")
    matches_simple.registerTempTable("simple")

//    // -- Duration Over Time --
//    val query_results = sqlContext.sql("SELECT match_id, ended_at, map_name, duration_seconds FROM simple")
//    val duration_results = query_results.map(row => (row.getInt(0), row.getFloat(1), row.getString(2), row.getInt(3)))
//    duration_results.saveToCassandra("matches_simple", "map_duration_over_time",
//      SomeColumns("match_id", "ended_at", "map_name", "duration_seconds"))

    // -- Duration Over Time by Day
    val duration_over_time = sqlContext.sql("SELECT match_id, ended_at, map_name, " +
      "duration_seconds FROM simple")
    val duration_over_time_day = duration_over_time.map(row => (row.getInt(0),
      (math floor row.getFloat(1)/24/3600)*24*3600, row.getString(2), row.getInt(3)))
    val duration_over_time_day_mapped = duration_over_time_day.map(row => ((row._2, row._3),
      row._4)).mapValues(x => (x,1)).reduceByKey((x,y) => (x._1 + y._1, x._2 + y._2))
    val duration_day_results = duration_over_time_day_mapped.map(row => (row._1._1, row._1._2,
      row._2._1.asInstanceOf[Float]/row._2._2.asInstanceOf[Float]/60))
    duration_day_results.saveToCassandra("matches_simple", "yolo_duration_all_day",
      SomeColumns("ended_at", "map_name", "duration_minutes"))

//     // -- Duration Over Time By Expansion --
//     val query_results = sqlContext.sql("SELECT match_id, ended_at, map_name, duration_seconds FROM simple WHERE player0_current_league_1v1 = 3")
// 
//     // -- Duration Over Time By Race --
//     val query_results = sqlContext.sql("SELECT match_id, ended_at, map_name, duration_seconds FROM simple WHERE  = 3")
// 

    // -- Top 10 Maps --
    // TODO: add url
    val top_10 = sqlContext.sql("SELECT map_name, count(map_name) as c FROM simple GROUP BY map_name ORDER BY c DESC LIMIT 10")
    val top_10_results = top_10.map(row => (row.getString(0), row.getLong(1)))
    top_10_results.saveToCassandra("matches_simple", "yolo_top_10",
      SomeColumns("map_name", "match_count"))


// 
//     // -- AUX --
//     // -- URL for Map --
//     // -- URL for Player --
//     // -- Player IDs by Match ID --
  }
}
