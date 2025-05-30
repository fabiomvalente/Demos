package com.aulaSpring.webservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aulaSpring.webservice.entities.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {

    
}
