package com.aulaSpring.webservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aulaSpring.webservice.entities.User;

public interface UserRepository extends JpaRepository<User, Long> {

    
}
