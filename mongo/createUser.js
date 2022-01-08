db.createUser({
  user: "staff",
  pwd: "password",
  roles: [{
    role: "readWrite",
    db: "test",
  }],
});
