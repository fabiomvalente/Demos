package com.cursojava.mongodb.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.cursojava.mongodb.domain.User;

@Repository
public interface UserRepository extends MongoRepository<User, String> {


}
