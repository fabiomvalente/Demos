package com.aulaSpring.webservice.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.aulaSpring.webservice.entities.Order;
import com.aulaSpring.webservice.repositories.OrderRepository;

@Service
public class OrderService {
    
    @Autowired
    private OrderRepository OrderRepository;

    public List<Order> findAll() {
        return OrderRepository.findAll();
    }

    public Order findById(Long id) {
        Optional<Order> obj = OrderRepository.findById(id);
        return obj.get();
    }
}
