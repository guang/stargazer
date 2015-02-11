import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.kafka._
import org.json4s._
import org.json4s.jackson.JsonMethods._
import org.json4s.JsonDSL._
import org.apache.log4j.Logger
import org.apache.log4j.Level
import com.datastax.spark.connector._
import com.datastax.spark.connector.streaming._
import com.datastax.driver.core.utils._


object StreamProcessing {
  def main(args: Array[String]) {

    val conf = new SparkConf().set("spark.cassandra.connection.host", "54.67.42.97")
    val ssc = new StreamingContext(conf, Seconds(5))

    val zk_quorum = "localhost:2181"
    val group_id = "spark_streaming"
    val topics = Map("recent_matches" -> 1)
    val kafka_stream = KafkaUtils.createStream(ssc, zk_quorum, group_id, topics)

    val parsed_message = kafka_stream.map( x => parse(x._2) )

    val recent_maps = parsed_message.map( message => (compact(render( message \ "map_name" )),
      compact(render( message \ "ended_at" ))))
    println("==================================================================")
    println("==================================================================")
    println("==================================================================")
    println(recent_maps.print())
    println("==================================================================")
    println("==================================================================")
    println("==================================================================")
    recent_maps.saveToCassandra("matches_simple", "yolo_recent_10",
      SomeColumns("map_name", "ended_at_raw"))

    ssc.start()
    ssc.awaitTermination()
  }
}
