import java.io.{ByteArrayInputStream, ByteArrayOutputStream}
import scala.sys.process._ // ProcessLogger + some implicits

// Seems to be a problem with Scala 2.12. Works with Scala 2.13.
object ProcessDeadlockRepro extends App {
  println("Scala Version: " + util.Properties.versionString)
  val inputText = "test"
  val outputStream = new ByteArrayOutputStream()
  val cmdResult: Process = (Seq("badcommand") #< new ByteArrayInputStream(inputText.getBytes()) #> outputStream).run(ProcessLogger(println, println))
  val exitValue = cmdResult.exitValue() // blocks forever
  println(s"Exit value: $exitValue") // doesn't run
}
