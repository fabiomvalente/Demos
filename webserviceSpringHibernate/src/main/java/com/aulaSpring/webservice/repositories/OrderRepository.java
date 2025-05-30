package com.aulaSpring.webservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aulaSpring.webservice.entities.Order;

public interface OrderRepository extends JpaRepository<Order, Long> {

    
}
