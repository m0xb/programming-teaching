import scala.annotation.tailrec

object Main {
  def main(args: Array[String]): Unit = {
    // Dots are optional for method calls:
    List(1,2,3) map {x => x*2}
    // De-sugars to:
    List(1,2,3).map({x => x*2})
    // Equivalent Haskell:
    // map (\x -> x*2) [1,2,3]

    val mylist = "foo" :: "bar" :: Nil
    // Equivalent Haskell:
    // mylist = "foo" : "bar" : []

    println(head(List("foo", "bar")))

    println(sumTR(5 :: 6 :: 7 :: Nil, 0))
  }

  // Compare with Haskell:
  // head :: [a] -> a
  // head [] = error "head of empty list"
  // head (x:_) = x
  def head[A](l: List[A]): A = l match {
    case Nil => throw new Exception("head of empty list")
    case a :: _ => a
  }

  def tail[A](l: List[A]): List[A] = l match {
    case Nil => throw new Exception("tail of empty list")
    case _ :: t => t
  }

  def length[A](l: List[A]): Int = l match {
    case Nil => 0
    case _ :: t => 1 + length(t)
  }

  @tailrec
  def lengthTR[A](l: List[A], acc: Int): Int =
    if (l.isEmpty) acc else lengthTR(l.tail, acc + 1)

  @tailrec
  def sumTR(l: List[Int], acc: Int): Int =
    if (l.isEmpty) acc else sumTR(l.tail, acc + l.head)

}