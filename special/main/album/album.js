/*
Author: fxzjshm
Licensed under MIT license.
*/

function addPhotos(imgNames){
    var l=imgNames.length;
    for (var i=0;i<l;i++){
        var liNode=document.createElement("li");
        var imgNode=document.createElement("img");
        imgNode.src=imgNames[i];
        imgNode.id="img"+i;
        liNode.appendChild(imgNode);
        document.getElementById("list1").appendChild(liNode);
        
        var aNode=document.createElement("a");
        aNode.href="#img"+i;
        var imgNode2=document.createElement("img");
        imgNode2.src=imgNames[i];
        aNode.appendChild(imgNode2);
        document.getElementById("chooser").appendChild(aNode);
    }
}

/*
Generate file names

File d=new File("E:\\1");
System.out.println(d.exists());
for(File f:d.listFiles()){
    System.out.println("\""+f.getName()+"\",");
}
*/