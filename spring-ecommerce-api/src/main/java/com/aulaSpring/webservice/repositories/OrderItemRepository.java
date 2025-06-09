package com.aulaSpring.webservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aulaSpring.webservice.entities.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long> {

    
}
