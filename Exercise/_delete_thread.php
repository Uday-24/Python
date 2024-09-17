<?php 
    include '_dbconnect.php';
    if(!$conn){
        exit();
    }
    $thread_id = $_GET['threadid'];
    $qry = "DELETE FROM threads WHERE thread_id = $thread_id";
    $qry2 = "DELETE FROM comments WHERE thread_id = $thread_id";
    $res = mysqli_query($conn, $qry);
    $res2 = mysqli_query($conn, $qry2);
    if($res && $res2){
        header('location: ../threadlist.php?cat_id='.$_GET["cat_id"]);
    }
    else{
        header('location: ../threadlist.php?cat_id='.$_GET["cat_id"]);
    }
?>