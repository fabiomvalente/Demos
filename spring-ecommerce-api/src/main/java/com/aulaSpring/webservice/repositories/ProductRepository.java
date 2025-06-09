package com.aulaSpring.webservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aulaSpring.webservice.entities.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {

    
}
