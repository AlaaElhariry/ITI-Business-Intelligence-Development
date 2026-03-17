//Insert one 
db.Staff.insertOne({
   _id: 1,        
   name: "Alaa",
   age: 23,
   gender: "female",
   department: "Data"
})

//inser Many
db.Staff.insertMany([
{
   _id: 2,
   name: "Ahmed",
   age: 20,
   gender: "male",
   department: "IT"
},
{
   _id: 3,
   name: "Sara",
   age: 25,
   gender: "female",
   managerName: "Ali",
   department: "HR"
},
{
   _id: 4,
   name: "Omar",
   age: 15,
   gender: "male",
   DOB: "2009-05-10"
}
])
//Queries
//Find All Documents
db.Staff.find()

//Find gender = male
db.Staff.find({gender: "male"})

//Age between 20 and 25
db.Staff.find({
   age: {$gte:20 , $lte:25}
})

//Age = 25 AND gender = female
db.Staff.find({
   age:25,
   gender:"female"
})

//Age = 20 OR gender = female
db.Staff.find({
   $or:[
      {age:20},
      {gender:"female"}
   ]
})


//Update One Document (age = 15)
db.Staff.updateOne(
   {age:15},
   {$set:{name:"Alaa Elhariry"}}
)

//Update Many Documents (department = AI
db.Staff.updateMany(
   {},
   {$set:{department:"AI"}}
)

//Create Collection "test" and Insert Documents

db.createCollection("test")

db.test.insertMany([
{
   _id:2,
   name:"Ahmed",
   age:20,
   gender:"male",
   department:"IT"
},
{
   _id:3,
   name:"Sara",
   age:25,
   gender:"female",
   managerName:"Ali",
   department:"HR"
},
{
   _id:4,
   name:"Omar",
   age:15,
   gender:"male",
   DOB:"2009-05-10"
}
])

//Delete One Document where age = 15
db.test.deleteOne({age:15})

//First insert
db.test.insertOne({_id:5, name:"ahmed", age:15})

//Second insert
db.test.insertOne({_id:6, name:"eman", age:15})

//When running deleteOne
db.test.deleteOne({age:15})

//Delete all documents where gender = male
db.test.deleteMany({gender:"male"})

//Delete all documents in the "test" collection
db.test.deleteMany({})
